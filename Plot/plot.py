#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkFileDialog
import pickle

class Plot():
    def save(domain_list):
        print("!!")
        f = tkFileDialog.asksaveasfile(mode='w', initialdir='/')
        liste_sauvegarde = pickle.Pickler(f)
        liste_sauvegarde.dump(domain_list)
        f.close()

    def load():
        print("!!!!!!")
        f = tkFileDialog.askopenfile(mode='r', initialdir='/')
        fname = f.name
        f.close()
        return pickle.load(file(fname))






