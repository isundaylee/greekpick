from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  letter_list = (
    ('alpha', ('Α', 'α')),
    ('beta', ('Β', 'β')),
    ('gamma', ('Γ', 'γ')),
    ('delta', ('Δ', 'δ')),
    ('epsilon', ('Ε', 'ε')),
    ('zeta', ('Ζ', 'ζ')),
    ('eta', ('Η', 'η')),
    ('theta', ('Θ', 'θ')),
    ('iota', ('Ι', 'ι')),
    ('kappa', ('Κ', 'κ')),
    ('lambda', ('Λ', 'λ')),
    ('mu', ('Μ', 'μ')),
    ('nu', ('Ν', 'ν')),
    ('xi', ('Ξ', 'ξ')),
    ('omicon', ('Ο', 'ο')),
    ('pi', ('Π', 'π')),
    ('rho', ('Ρ', 'ρ')),
    ('sigma', ('Σ', 'σ')),
    ('tau', ('Τ', 'τ')),
    ('upsilon', ('Υ', 'υ')),
    ('phi', ('Φ', 'φ')),
    ('chi', ('Χ', 'χ')),
    ('psi', ('Ψ', 'ψ')),
    ('omega', ('Ω', 'ω'))
  )

  return render(request, 'index.html', {
    'letters': letter_list
  })


def vote(request, letter):
  return HttpResponse(letter)
