---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_ray_count",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-lines/alpha-ray-count/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.Lines`.",
  "declaration_id": "TauLib.BookII.Transcendentals.Lines::alpha_ray_count",
  "declaration_slug": "alpha-ray-count",
  "kind": "def",
  "name": "alpha_ray_count",
  "module_name": "TauLib.BookII.Transcendentals.Lines",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-lines/",
  "source_line_start": 41,
  "source_line_end": 48,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Lines.lean#L41-L48",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Lines.lean#L41-L48",
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
- Source path: [`TauLib/BookII/Transcendentals/Lines.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Lines.lean#L41-L48)
- Source range: L41-L48
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Count alpha-ray members in [2, bound] for a given prime a. -/
```

## Source Excerpt

```lean
def alpha_ray_count (a bound : TauIdx) : Nat :=
  go 2 (bound + 1) 0
where
  go (x fuel acc : Nat) : Nat :=
    if fuel = 0 then acc
    else if x > bound then acc
    else go (x + 1) (fuel - 1) (acc + if alpha_ray_member x a then 1 else 0)
  termination_by fuel
```
