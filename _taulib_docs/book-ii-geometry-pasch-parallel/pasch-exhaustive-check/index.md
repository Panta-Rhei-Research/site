---
{
  "projection_kind": "taulib_declaration",
  "title": "pasch_exhaustive_check",
  "permalink": "/verify/taulib/docs/book-ii-geometry-pasch-parallel/pasch-exhaustive-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.PaschParallel`.",
  "declaration_id": "TauLib.BookII.Geometry.PaschParallel::pasch_exhaustive_check",
  "declaration_slug": "pasch-exhaustive-check",
  "kind": "def",
  "name": "pasch_exhaustive_check",
  "module_name": "TauLib.BookII.Geometry.PaschParallel",
  "module_url": "/verify/taulib/docs/book-ii-geometry-pasch-parallel/",
  "source_line_start": 66,
  "source_line_end": 75,
  "registry_ids": [
    "II.T17"
  ],
  "related_registry_items": [
    {
      "id": "II.T17",
      "title": "Pasch Axiom",
      "url": "/registry/object/II.T17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/PaschParallel.lean#L66-L75",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Geometry.PaschParallel",
        "url": "/verify/taulib/docs/book-ii-geometry-pasch-parallel/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/PaschParallel.lean#L66-L75",
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

- Module: [TauLib.BookII.Geometry.PaschParallel](/verify/taulib/docs/book-ii-geometry-pasch-parallel/)
- Source path: [`TauLib/BookII/Geometry/PaschParallel.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/PaschParallel.lean#L66-L75)
- Source range: L66-L75
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T17` — Pasch Axiom

## Immediate Comment / Docstring

```lean
/-- [II.T17] Exhaustive collinearity check for all triples in [2, bound].
    Flat triple loop with single fuel counter. -/
```

## Source Excerpt

```lean
def pasch_exhaustive_check (bound db : TauIdx) : Bool :=
  go 2 2 2 ((bound + 1) * (bound + 1) * (bound + 1))
where
  go (a b c fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a > bound then true
    else if b > bound then go (a + 1) 2 2 (fuel - 1)
    else if c > bound then go a (b + 1) 2 (fuel - 1)
    else collinear_triple a b c db && go a b (c + 1) (fuel - 1)
  termination_by fuel
```
