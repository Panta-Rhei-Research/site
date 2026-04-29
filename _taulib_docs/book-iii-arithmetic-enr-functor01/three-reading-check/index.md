---
{
  "projection_kind": "taulib_declaration",
  "title": "three_reading_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-enr-functor01/three-reading-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.EnrFunctor01`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.EnrFunctor01::three_reading_check",
  "declaration_slug": "three-reading-check",
  "kind": "def",
  "name": "three_reading_check",
  "module_name": "TauLib.BookIII.Arithmetic.EnrFunctor01",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-enr-functor01/",
  "source_line_start": 112,
  "source_line_end": 121,
  "registry_ids": [
    "III.P24"
  ],
  "related_registry_items": [
    {
      "id": "III.P24",
      "title": "Three-Reading Equivalence at E₁",
      "url": "/registry/object/III.P24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L112-L121",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.EnrFunctor01",
        "url": "/verify/taulib/docs/book-iii-arithmetic-enr-functor01/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L112-L121",
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

- Module: [TauLib.BookIII.Arithmetic.EnrFunctor01](/verify/taulib/docs/book-iii-arithmetic-enr-functor01/)
- Source path: [`TauLib/BookIII/Arithmetic/EnrFunctor01.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L112-L121)
- Source range: L112-L121
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P24` — Three-Reading Equivalence at E₁

## Immediate Comment / Docstring

```lean
/-- [III.P24] Three-reading equivalence: the E₁ MD instance has exactly
    three non-trivial sector-restricted readings: NS, YM, Hodge. -/
```

## Source Excerpt

```lean
def three_reading_check (bound db : TauIdx) : Bool :=
  -- Reading 1: NS (flow dynamics on B/C sectors)
  let ns := ns_component_check bound db
  -- Reading 2: YM (spectral gap in gauge sector)
  let ym := ym_component_check db
  -- Reading 3: Hodge (filtration + addressability)
  let hodge := hodge_component_check bound db
  -- All three readings are non-trivially different
  -- (each checks something the others don't)
  ns && ym && hodge
```
