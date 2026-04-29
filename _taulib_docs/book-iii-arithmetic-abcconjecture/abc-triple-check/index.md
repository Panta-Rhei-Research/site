---
{
  "projection_kind": "taulib_declaration",
  "title": "abc_triple_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-abcconjecture/abc-triple-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.ABCConjecture`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ABCConjecture::abc_triple_check",
  "declaration_slug": "abc-triple-check",
  "kind": "def",
  "name": "abc_triple_check",
  "module_name": "TauLib.BookIII.Arithmetic.ABCConjecture",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-abcconjecture/",
  "source_line_start": 110,
  "source_line_end": 121,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L110-L121",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L110-L121",
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
- Source path: [`TauLib/BookIII/Arithmetic/ABCConjecture.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L110-L121)
- Source range: L110-L121
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D98` — ABC Quality

## Immediate Comment / Docstring

```lean
/-- [III.D98] ABC quality check for a triple (a, b, c=a+b):
    verify c < rad(a·b·c)^2. This is a weak form of ABC (ε=1). -/
```

## Source Excerpt

```lean
def abc_triple_check (a b : Nat) : Bool :=
  if a == 0 || b == 0 then true
  else
    let c := a + b
    -- Require gcd(a, b) = 1 (coprime)
    let g := Nat.gcd a b
    if g != 1 then true  -- skip non-coprime triples
    else
      let abc := a * b * c
      let r := radical abc
      -- Weak ABC: c < rad(abc)^2
      r > 0 && c < r * r
```
