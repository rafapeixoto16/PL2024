# TPC6 : GIC LL(1) 

## Enunciado

Fazer a gramatica indepente de contexto para a seguinte "linguagem":

- ? a
- b = a * 2 / (27 - 3)
- ! a + b
- c = a * b / (a / b)

## Autor

- A96807
- Rafael Conde Peixoto

## Solução obtida 

Esta foi a solução desenvolvida:

Simbolos terminais T = {"?","=","*","/","+","-",")","(","!",number,var}

```

Produções                                           Look ahead

Regras S -> Programa S                              {"?","!","var"}                              
          | &                                       {"$"}

Programa -> "?" Var                                 {"?"}
          | "!" operaçao                            {"!"}
          | var = operacao                          {"var"}

operaçao -> Factor operacao2                        {var,number,"("}

operacao2  -> "+" Factor                            {"+"}
            | "-" Factor                            {"-"}
            | &                                     {")"} *verificar

Factor -> Termo Factor2                             {var,number,")"}

Factor2 -> "*" Termo                                {"*"}
         | "/" Termo                                {"/"}
         | &                                        {"+","-"} *verificar

Termo -> Var                                        {Var}
       | number                                     {number}
       | "(" operaçao ")"                           {"("}

```