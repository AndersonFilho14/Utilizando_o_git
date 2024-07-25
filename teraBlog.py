# Git merge
    Serve para mesclar uma branch com outra. Vc deve estar no diretorio que recebera o merg e usar 
    'git merge <nome_da_branch>'

#Git pull
    Traz todas as alterações do github,(serve para atualizar a sua maquina) 
    "git pull origin http"

#Git rm
    para apagar um arquivo do commit de forma segura
    'git rm <nome_do_arquivo>'
    para voltar com ele, busque o commit que ele estava presente e use 
    'git checkout <hash_do_commit>~1 <nome do arquivo a ser resgatado dentro daquele commit>'


#Git stash
    Se um projeto que ir pra outra branch, e não quer levar o projeto inacabado para outra branch se usa o 
    'git stash'
    depois que ver oque tinha que ser feito, para voltar o stash.usa:
        'git stash apply <stash>'   Uso: Quando você deseja aplicar as mudanças da stash, mas ainda quer manter a stash para poder aplicá-la novamente ou em outro lugar.
        'git stash pop <stash>' Uso: Quando você deseja aplicar as mudanças da stash e não precisa mais dela depois de aplicá-la.
    'git stash list' mostras os stash que foram feitos
    'git stash clear' limpa os stash 

#git config 
    O config é um comando inicial para vincular o trabalho no repositório com sua conta no github. Assim, é configurado com o nome e com o e-mail. 
    'git config --global user.name "<nome>'
    'git config --global user.email <email>'
    