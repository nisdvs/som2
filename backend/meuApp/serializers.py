from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','nome','telefone','categoria','groups']
        many = True
        
class FormatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formato
        fields ='__all__'
        many = True


class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Foto
        fields = '__all__'
        many = True

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'
        many = True


class CategoriaLivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaLivro
        fields = '__all__'
        many = True

    
class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['nome', 'ano', 'qtd_paginas', 'numero_edicao', 'descricao', ' valor_emprestimo', 'qtd_estoque', 'estrelas', 'imagem_capa', 'status', ]
        many = True  


class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model: Emprestimo
        fiels = ['data_emprestimo', 'data_devolucao_prevista', ' data_devolucao_realizada', 'valor_total_emprestimo', 'status']
        many = True 

        
class itemEmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model: itemEmprestimo
        fiels = ['livroFK', 'emprestimoFK']
        many = True
