## Simulações de Dispersão de Poluentes com OpenFOAM

Bem-vindo ao repositório Simulações de Dispersão de Poluentes com OpenFOAM! Este repositório contém uma coleção de casos de simulação e scripts para modelar a dispersão de poluentes usando o OpenFOAM, uma ferramenta de código aberto para dinâmica dos fluidos computacional (CFD).

### Estrutura do Repositório

A estrutura do repositório está organizada da seguinte maneira:

```
/simulacoes
    /caso1
        /0
        /constant
        /system
    /caso2
        /0
        /constant
        /system
/scripts
    - Em desenvolvimento
/docs
    - Material complementar
README.md
```

- /simulacões: Contém os diferentes casos de simulação.
- /scripts: Scripts auxiliares para preprocessamento e pós-processamento das simulações.
- /doc: Documentação adicional e tutoriais.


### Instalação

Para utilizar os casos de simulação, é necessário ter o OpenFOAM instalado em seu sistema. Você pode seguir as instruções oficiais de instalação do OpenFOAM disponíveis [aqui](https://develop.openfoam.com/Development/openfoam/-/wikis/precompiled) com alguns tutoriais disponíveis [aqui](https://wiki.openfoam.com/Main_Page)

### Uso

Para rodar uma simulação, siga os passos abaixo:

1. Navegue até o diretório do caso de simulação desejado, por exemplo, caso1:

```
cd simulacoes/caso1
```

2. Execute o script de configuração inicial (maioria dos casos já implementado):

```
./Allrun
```

3. Ou inicie a simulação utilizando o comando do OpenFOAM adequado, por exemplo:

```
blockMesh
simpleFoam
```

Para detalhes específicos de cada caso, consulte a documentação ou wiki.

### Visualização do resultado

Recomenda-se utilizar o ParaView, disponível [aqui](https://www.paraview.org/download/). Para utiliza-ló, digite *paraFoam* no terminal após a execução do solver ser finalizada.











