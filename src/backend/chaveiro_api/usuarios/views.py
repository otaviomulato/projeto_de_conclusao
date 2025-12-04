from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Usuario
import json

@csrf_exempt
@require_POST
def register_api(request):
    try:
        data = json.loads(request.body)
        
        # Check if email already exists
        if Usuario.objects.filter(email_user=data.get('email')).exists():
            return JsonResponse({'status': 'error', 'message': 'Email já cadastrado.'}, status=400)

        usuario = Usuario.objects.create(
            nome_user=data.get('nome'),
            email_user=data.get('email'),
            senha_user=data.get('senha'), # Note: In production, hash this password!
            telefone=data.get('telefone'),
            profissao=data.get('profissao'),
            idade=int(data.get('idade')),
            credito=0
        )
        
        # Set session
        request.session['user_id'] = usuario.id
        request.session['user_name'] = usuario.nome_user
        
        return JsonResponse({'status': 'success', 'message': 'Usuário cadastrado com sucesso!'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@csrf_exempt
@require_POST
def login_api(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')
        senha = data.get('senha')
        
        try:
            usuario = Usuario.objects.get(email_user=email, senha_user=senha)
            
            # Set session
            request.session['user_id'] = usuario.id
            request.session['user_name'] = usuario.nome_user
            
            return JsonResponse({
                'status': 'success', 
                'message': 'Login realizado com sucesso!',
                'user': {
                    'nome': usuario.nome_user,
                    'email': usuario.email_user,
                    'credito': usuario.credito
                }
            })
        except Usuario.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Email ou senha inválidos.'}, status=401)
            
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)