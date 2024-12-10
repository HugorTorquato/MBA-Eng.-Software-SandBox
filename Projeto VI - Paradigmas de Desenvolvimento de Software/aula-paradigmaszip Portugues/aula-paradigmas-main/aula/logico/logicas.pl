pai(jose, maria)
pai(jose, joao)
mae(ana, maria)
mae(ana, joao)
pai(marcos, jose)
mae(clarice, jose)
pai(pedro, ana)
mae(renata, ana)

# Podemos ter referencias que não estamos vendo, forma diferente de pensar e resolver o problem

eh_pai(Pai, Filho) :-
    pai(Pai, Filho).

eh_mae(Mae, Filho) :-
    mae(Mae, Filho).

eh_avo(Avo, Neto) :-
    pai(Avo, Pai),
    pai(Pai, Neto).