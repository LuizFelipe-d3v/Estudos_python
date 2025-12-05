from datetime import datetime

class Usuario:
    def __init__(self, id, nome, login, senha):
        self.id = id
        self.nome = nome
        self.login = login
        self.senha = senha
        self.autenticado = False

    def autenticar(self, login, senha):
        if self.login == login and self.senha == senha:
            self.autenticado = True
            print(f"Usuário {self.nome} autenticado com sucesso!")
        else:
            print("Falha na autenticação.")


class Postagem:
    def __init__(self, id, titulo, texto, usuario, data_publicacao=None):
        self.id = id
        self.titulo = titulo
        self.texto = texto
        self.usuario = usuario      # Usuario que criou
        self.data_publicacao = data_publicacao  # None = ainda não publicado

    def __str__(self):
        data = self.data_publicacao.strftime("%d/%m/%Y %H:%M") if self.data_publicacao else "A definir"
        return f"[{self.id}] {self.titulo} - por {self.usuario.nome} | Publicação: {data}"


class Blog:
    def __init__(self):
        self.postagens = []

    def adicionarPostagem(self, postagem):
        self.postagens.append(postagem)
        print(f"Postagem '{postagem.titulo}' adicionada.")

    def publicarPostagem(self, postagem):
        postagem.data_publicacao = datetime.now()
        print(f"Postagem '{postagem.titulo}' publicada em {postagem.data_publicacao}.")

    def listarTodasAsPostagens(self):
        print("\n--- TODAS AS POSTAGENS ---")
        for p in self.postagens:
            print(p)

    def listarPostagensPublicadas(self):
        print("\n--- POSTAGENS PUBLICADAS ---")
        agora = datetime.now()
        for p in self.postagens:
            if p.data_publicacao is not None and p.data_publicacao <= agora:
                print(p)

    def apagarPostagem(self, postagem):
        if postagem in self.postagens:
            self.postagens.remove(postagem)
            print(f"Postagem '{postagem.titulo}' removida.")


u1 = Usuario(1, "Ana", "ana123", "senha")


u1.autenticar("ana123", "senha")


blog = Blog()


if u1.autenticado:
    p1 = Postagem(1, "Meu primeiro post", "Conteúdo do post...", u1)
    blog.adicionarPostagem(p1)


blog.publicarPostagem(p1)


blog.listarPostagensPublicadas()


blog.listarTodasAsPostagens()
