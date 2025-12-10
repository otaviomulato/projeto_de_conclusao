from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods
from .models import Usuario
import json

# --- 1. API DE REGISTRO (Esta é a que estava faltando!) ---
@csrf_exempt
@require_POST
def register_api(request):
    try:
        data = json.loads(request.body)
        
        # Verifica email duplicado
        if Usuario.objects.filter(email_user=data.get('email')).exists():
            return JsonResponse({'status': 'error', 'message': 'Email já cadastrado.'}, status=400)

        # Cria usuário
        usuario = Usuario.objects.create(
            nome_user=data.get('nome'),
            email_user=data.get('email'),
            senha_user=data.get('senha'), 
            telefone=data.get('telefone'),
            profissao=data.get('profissao'),
            idade=int(data.get('idade')),
            credito=int(data.get('credito'))
        )
        
        # Loga automaticamente
        request.session['user_id'] = usuario.id
        request.session['user_name'] = usuario.nome_user
        
        return JsonResponse({'status': 'success', 'message': 'Usuário cadastrado com sucesso!'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

# --- 2. API DE LOGIN ---
@csrf_exempt
@require_POST
def login_api(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')
        senha = data.get('senha')
        
        try:
            usuario = Usuario.objects.get(email_user=email, senha_user=senha)
            
            # Verifica se conta foi excluída
            if not usuario.is_active:
                return JsonResponse({'status': 'error', 'message': 'Esta conta foi desativada.'}, status=403)

            # Salva na sessão
            request.session['user_id'] = usuario.id
            request.session['user_name'] = usuario.nome_user
            
            return JsonResponse({'status': 'success', 'message': 'Login realizado!'})
        except Usuario.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Email ou senha inválidos.'}, status=401)
            
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

# --- 3. API DE PERFIL (Para carregar e editar dados) ---
@csrf_exempt
@require_http_methods(["GET", "PUT"])
def profile_api(request):
    user_id = request.session.get('user_id')
    
    # Se não tiver sessão, retorna erro 401
    if not user_id:
        return JsonResponse({'status': 'error', 'message': 'Usuário não logado'}, status=401)
        
    try:
        usuario = Usuario.objects.get(id=user_id)
        
        # GET: Envia dados para o HTML
        if request.method == "GET":
            return JsonResponse({
                'status': 'success',
                'data': {
                    'nome': usuario.nome_user,
                    'email': usuario.email_user,
                    'telefone': usuario.telefone,
                    'profissao': usuario.profissao,
                    'idade': usuario.idade,
                    'senha': usuario.senha_user 
                }
            })
            
        # PUT: Recebe dados para salvar
        if request.method == "PUT":
            data = json.loads(request.body)
            
            usuario.nome_user = data.get('nome', usuario.nome_user)
            usuario.telefone = data.get('telefone', usuario.telefone)
            usuario.profissao = data.get('profissao', usuario.profissao)
            usuario.idade = data.get('idade', usuario.idade)
            usuario.credito = data.get('credito', usuario.credito)
            
            nova_senha = data.get('senha')
            if nova_senha and nova_senha.strip() != "":
                usuario.senha_user = nova_senha
                
            usuario.save()
            
            # Atualiza nome na sessão
            request.session['user_name'] = usuario.nome_user
            
            return JsonResponse({'status': 'success', 'message': 'Dados atualizados!'})

    except Usuario.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Usuário não encontrado'}, status=404)

# --- 4. API DE DESATIVAR CONTA ---
@csrf_exempt
@require_http_methods(["DELETE"])
def deactivate_account(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse({'status': 'error', 'message': 'Não autorizado'}, status=401)
    
    try:
        usuario = Usuario.objects.get(id=user_id)
        usuario.is_active = False # Soft delete
        usuario.save()
        request.session.flush() # Logout
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

# --- 5. LOGOUT ---
def logout_view(request):
    request.session.flush()
    return redirect('index')