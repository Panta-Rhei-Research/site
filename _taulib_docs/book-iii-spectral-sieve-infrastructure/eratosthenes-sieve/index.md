---
{
  "projection_kind": "taulib_declaration",
  "title": "eratosthenes_sieve",
  "permalink": "/corpus/taulib/docs/book-iii-spectral-sieve-infrastructure/eratosthenes-sieve/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.SieveInfrastructure`.",
  "declaration_id": "TauLib.BookIII.Spectral.SieveInfrastructure::eratosthenes_sieve",
  "declaration_slug": "eratosthenes-sieve",
  "kind": "def",
  "name": "eratosthenes_sieve",
  "module_name": "TauLib.BookIII.Spectral.SieveInfrastructure",
  "module_url": "/corpus/taulib/docs/book-iii-spectral-sieve-infrastructure/",
  "source_line_start": 74,
  "source_line_end": 75,
  "registry_ids": [
    "III.D99"
  ],
  "related_registry_items": [
    {
      "id": "III.D99",
      "title": "Eratosthenes Sieve",
      "url": "/registry/object/III.D99/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L74-L75",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.SieveInfrastructure",
        "url": "/corpus/taulib/docs/book-iii-spectral-sieve-infrastructure/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L74-L75",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIII.Spectral.SieveInfrastructure](/corpus/taulib/docs/book-iii-spectral-sieve-infrastructure/)
- Source path: [`TauLib/BookIII/Spectral/SieveInfrastructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L74-L75)
- Source range: L74-L75
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.D99` — Eratosthenes Sieve

## Immediate Comment / Docstring

```lean
/-- [III.D99] Sieve of Eratosthenes: primality test via trial division. -/
```

## Source Excerpt

```lean
def eratosthenes_sieve (n : Nat) : Bool :=
  is_prime_sieve n
```
