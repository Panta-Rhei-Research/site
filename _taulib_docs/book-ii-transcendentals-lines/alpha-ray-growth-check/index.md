---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_ray_growth_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-lines/alpha-ray-growth-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.Lines`.",
  "declaration_id": "TauLib.BookII.Transcendentals.Lines::alpha_ray_growth_check",
  "declaration_slug": "alpha-ray-growth-check",
  "kind": "def",
  "name": "alpha_ray_growth_check",
  "module_name": "TauLib.BookII.Transcendentals.Lines",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-lines/",
  "source_line_start": 106,
  "source_line_end": 115,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Lines.lean#L106-L115",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.Lines",
        "url": "/verify/taulib/docs/book-ii-transcendentals-lines/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Lines.lean#L106-L115",
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

- Module: [TauLib.BookII.Transcendentals.Lines](/verify/taulib/docs/book-ii-transcendentals-lines/)
- Source path: [`TauLib/BookII/Transcendentals/Lines.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Lines.lean#L106-L115)
- Source range: L106-L115
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Alpha-ray growth: more D-residues appear at higher stages.
    count_d_residues(k) <= count_d_residues(k+1) (monotone refinement). -/
```

## Source Excerpt

```lean
def alpha_ray_growth_check (a bound stages : TauIdx) : Bool :=
  go 1 (stages + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > stages then true
    else
      count_d_residues a k bound <= count_d_residues a (k + 1) bound &&
      go (k + 1) (fuel - 1)
  termination_by fuel
```
