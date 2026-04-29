---
{
  "projection_kind": "taulib_declaration",
  "title": "radical_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-abcconjecture/radical-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.ABCConjecture`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ABCConjecture::radical_check",
  "declaration_slug": "radical-check",
  "kind": "def",
  "name": "radical_check",
  "module_name": "TauLib.BookIII.Arithmetic.ABCConjecture",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-abcconjecture/",
  "source_line_start": 89,
  "source_line_end": 102,
  "registry_ids": [
    "III.D97"
  ],
  "related_registry_items": [
    {
      "id": "III.D97",
      "title": "Radical Function",
      "url": "/registry/object/III.D97/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L89-L102",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L89-L102",
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
- Source path: [`TauLib/BookIII/Arithmetic/ABCConjecture.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L89-L102)
- Source range: L89-L102
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D97` — Radical Function

## Immediate Comment / Docstring

```lean
/-- [III.D97] Radical check: verify rad(n) divides n and rad(rad(n)) = rad(n)
    (idempotence) for all n up to bound. -/
```

## Source Excerpt

```lean
def radical_check (bound : Nat) : Bool :=
  go 1 (bound + 1)
where
  go (n fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n > bound then true
    else
      let r := radical n
      -- rad(n) | n
      let divides := n == 0 || (r > 0 && n % r == 0)
      -- rad(rad(n)) = rad(n) (idempotent: radical is squarefree)
      let idempotent := radical r == r
      divides && idempotent && go (n + 1) (fuel - 1)
  termination_by fuel
```
