---
{
  "projection_kind": "taulib_declaration",
  "title": "abc_quality_bound_check",
  "permalink": "/corpus/taulib/docs/book-iii-arithmetic-abcconjecture/abc-quality-bound-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.ABCConjecture`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ABCConjecture::abc_quality_bound_check",
  "declaration_slug": "abc-quality-bound-check",
  "kind": "def",
  "name": "abc_quality_bound_check",
  "module_name": "TauLib.BookIII.Arithmetic.ABCConjecture",
  "module_url": "/corpus/taulib/docs/book-iii-arithmetic-abcconjecture/",
  "source_line_start": 125,
  "source_line_end": 134,
  "registry_ids": [
    "III.D98"
  ],
  "related_registry_items": [
    {
      "id": "III.D98",
      "title": "ABC Quality",
      "url": "/registry/object/III.D98/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L125-L134",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.ABCConjecture",
        "url": "/corpus/taulib/docs/book-iii-arithmetic-abcconjecture/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L125-L134",
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

- Module: [TauLib.BookIII.Arithmetic.ABCConjecture](/corpus/taulib/docs/book-iii-arithmetic-abcconjecture/)
- Source path: [`TauLib/BookIII/Arithmetic/ABCConjecture.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L125-L134)
- Source range: L125-L134
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.D98` — ABC Quality

## Immediate Comment / Docstring

```lean
/-- [III.D98] ABC quality bound check: for all coprime pairs (a,b) with
    a, b ≤ bound, verify c < rad(abc)^2. -/
```

## Source Excerpt

```lean
def abc_quality_bound_check (bound : Nat) : Bool :=
  go 1 1 ((bound + 1) * (bound + 1))
where
  go (a b fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a > bound then true
    else if b > bound then go (a + 1) 1 (fuel - 1)
    else
      abc_triple_check a b && go a (b + 1) (fuel - 1)
  termination_by fuel
```
