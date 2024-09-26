#Napište funkci double(a, b), která vypíše informaci o tom, zda b je dvojnásobkem a (viz ukázkový výstup). Máte připravený kód, který bude potřeba trochu opravit.

def double(a, b):
    if b/2 == a:
        print(b, "je dvojnasobek", a)
    else:
        print(b, "neni dvojnasobek", a)
