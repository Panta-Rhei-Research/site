---
{
  "projection_kind": "taulib_declaration",
  "title": "radical_le_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-abcconjecture/radical-le-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.ABCConjecture`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ABCConjecture::radical_le_check",
  "declaration_slug": "radical-le-check",
  "kind": "def",
  "name": "radical_le_check",
  "module_name": "TauLib.BookIII.Arithmetic.ABCConjecture",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-abcconjecture/",
  "source_line_start": 173,
  "source_line_end": 182,
  "registry_ids": [
    "III.P41"
  ],
  "related_registry_items": [
    {
      "id": "III.P41",
      "title": "Radical-Primorial Identity",
      "url": "/registry/object/III.P41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L173-L182",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.ABCConjecture",
        "url": "/verify/taulib/docs/book-iii-arithmetic-abcconjecture/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L173-L182",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookIII.Arithmetic.ABCConjecture](/verify/taulib/docs/book-iii-arithmetic-abcconjecture/)
- Source path: [`TauLib/BookIII/Arithmetic/ABCConjecture.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L173-L182)
- Source range: L173-L182
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P41` — Radical-Primorial Identity

## Immediate Comment / Docstring

```lean
/-- [III.P41] Extended: rad(n) ≤ n for all n, with equality iff n is
    squarefree. At primorial levels, equality holds. -/
```

## Source Excerpt

```lean
def radical_le_check (bound : Nat) : Bool :=
  go 1 (bound + 1)
where
  go (n fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n > bound then true
    else
      let r := radical n
      (r <= n) && go (n + 1) (fuel - 1)
  termination_by fuel
```
