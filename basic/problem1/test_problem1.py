# test_filtrar_numeros.py
import builtins
from problem1 import main
import pytest

def test_pares(monkeypatch, capsys):
    inputs = iter(["5", "2 5 9 6 1", "0"])
    monkeypatch.setattr(builtins, "input", lambda: next(inputs))

    main()

    salida = capsys.readouterr().out.strip()
    assert salida == "2 6"

def test_impares(monkeypatch, capsys):
    inputs = iter(["5", "2 5 9 6 1", "1"])
    monkeypatch.setattr(builtins, "input", lambda: next(inputs))

    main()

    salida = capsys.readouterr().out.strip()
    assert salida == "5 9 1"
