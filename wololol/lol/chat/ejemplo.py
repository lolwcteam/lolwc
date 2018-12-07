#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Client

clientes = []
nosalir = True

try:
    while nosalir:
        a = raw_input("usuario> ")
        b = raw_input("contraseña> ")
        if a == "send":
            to = raw_input("to> ")
            msg = raw_input("msg> ")
            clientes[b].send(to, msg)
        elif a == "show":
            for i in clientes:
                print(i.jid)
        else:
            cliente = Client.Cliente(a, b, "las")
            if cliente.connected:
                for i in range(len(clientes)):
                    if clientes[i].jid == cliente.jid:
                        clientes.pop(i)
                        break
                clientes.append(cliente)
except KeyboardInterrupt:
    for i in clientes:
        i.close("Cerrando "+str(i.name))
    print("Adios!")
