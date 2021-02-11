#!/usr/bin/python3
# bot.py
# bot do Discord para o cursinho
# joao-zonzini 08/02/21

#imports das bibliotecas
import discord
from discord.ext import commands    ## comandos do bot
import os                           ## comandos do sistema operacional
import random                       ## coisas aleatorias
from dotenv import load_dotenv      ## para pegar as variaveis do ambiente

import utils.calc as calc

## carregando as variaveis
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

## configurando bot
bot = commands.Bot(command_prefix='!')   ## todo comando deve começar com ! para o bot identificar

@bot.event
async def on_ready():                                       ## assim que o bot conectar ao Discord
    print(f'{bot.user.name} está conectado ao Discord!')    ## emite mensagem de conexao no terminal


@bot.event
async def on_member_join():                                 ## quando alguem entrar no servidor
    await member.create.dm()
    await member.dm_channel.send(f'{member.name}, bem vindo ao servidor do Cursinho!')  ## manda dm para o novo

@bot.event
async def on_message(message):
    if bot.user.id != message.author.id:                            ## verifica se o bot nao falou
        if 'tchau' in message.content.lower():                      ## ver tchau na mensagem com lower
            await message.channel.send('Fica, vai ter bolo...')     ## em homenagem ao Ian
            await message.channel.send('🎂')                        ## emoji de bolo

        await bot.process_commands(message)                         ## processa a mensagem pelos comandos

@bot.command(name='calc', help='Realiza operacoes matematicas com dois numeros')
async def calcular(ctx, primeiro: float, operador, segundo: float):   ## tudo eh string, dois pontos converte
    if operador == '+':
        resultado = calc.somar(primeiro, segundo)
    elif operador == '-':
        resultado = calc.somar(primeiro, -segundo)
    elif operador == '*':
        resultado = calc.mult(primeiro, segundo)
    elif operador == '**':
        resultado = calc.potenc(primeiro, segundo)
    else:
        resultado = 'Não conheço esse operador ;('
    await ctx.send(resultado)


@bot.command(name='criar_canal', help='Cria canal com nome dado')
## @commands.has_role('cargo')                          ## se quisermos limitar o comando a certo cargo
async def criar_canal(ctx, nome_canal):
    guild = ctx.guild                                   ## guild eh o servidor
    ja_existe = discord.utils.get(guild.channels, name=channel_name)  ## verifica se existe canal com o nome
    if not ja_existe:                                   ## caso nao exista, crie
        print(f'Criando canal de nome: {nome_canal}')   ## confirmacao no terminal
        await guild.create_text_channel(nome_canal)     ## enfim cria canal


bot.run(TOKEN)
