---
{
  "projection_kind": "taulib_declaration",
  "title": "norm_positivity_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-l2-space/norm-positivity-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.L2Space`.",
  "declaration_id": "TauLib.BookII.Hartogs.L2Space::norm_positivity_check",
  "declaration_slug": "norm-positivity-check",
  "kind": "def",
  "name": "norm_positivity_check",
  "module_name": "TauLib.BookII.Hartogs.L2Space",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-l2-space/",
  "source_line_start": 84,
  "source_line_end": 94,
  "registry_ids": [
    "II.D83"
  ],
  "related_registry_items": [
    {
      "id": "II.D83",
      "title": "L² Norm",
      "url": "/registry/object/II.D83/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L84-L94",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.L2Space",
        "url": "/verify/taulib/docs/book-ii-hartogs-l2-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L84-L94",
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

- Module: [TauLib.BookII.Hartogs.L2Space](/verify/taulib/docs/book-ii-hartogs-l2-space/)
- Source path: [`TauLib/BookII/Hartogs/L2Space.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L84-L94)
- Source range: L84-L94
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D83` — L² Norm

## Immediate Comment / Docstring

```lean
/-- [II.D83] Positivity check: ‖f‖² ≥ 0. -/
```

## Source Excerpt

```lean
def norm_positivity_check (k : Nat) : Bool :=
  let pk := primorial k
  go 0 pk
where
  go (seed fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if seed >= 6 then true
    else
      let f : Nat → Int := fun x => (x + seed : Int)
      l2_norm_sq f k >= 0 && go (seed + 1) (fuel - 1)
  termination_by fuel
```
