---
{
  "projection_kind": "taulib_declaration",
  "title": "bndlift_existence_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/bndlift-existence-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.BndLift`.",
  "declaration_id": "TauLib.BookII.Hartogs.BndLift::bndlift_existence_check",
  "declaration_slug": "bndlift-existence-check",
  "kind": "def",
  "name": "bndlift_existence_check",
  "module_name": "TauLib.BookII.Hartogs.BndLift",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/",
  "source_line_start": 146,
  "source_line_end": 156,
  "registry_ids": [
    "II.T26"
  ],
  "related_registry_items": [
    {
      "id": "II.T26",
      "title": "BndLift Existence",
      "url": "/registry/object/II.T26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L146-L156",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.BndLift",
        "url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L146-L156",
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

- Module: [TauLib.BookII.Hartogs.BndLift](/verify/taulib/docs/book-ii-hartogs-bnd-lift/)
- Source path: [`TauLib/BookII/Hartogs/BndLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L146-L156)
- Source range: L146-L156
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T26` — BndLift Existence

## Immediate Comment / Docstring

```lean
/-- [II.T26] BndLift existence theorem (tower coherence).
    For all x in [2, bound] and stages in [1, k_max]:
    reduce(bndlift(x, n), n) = reduce(x, n).

    This is a direct consequence of reduction_compat: since
    bndlift(x, n) = reduce(x, n+1), we have
    reduce(reduce(x, n+1), n) = reduce(x, n) because n ≤ n+1. -/
```

## Source Excerpt

```lean
def bndlift_existence_check (k_max bound : TauIdx) : Bool :=
  go 1 2 (k_max * bound + k_max + bound + 1)
where
  go (stage x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if stage > k_max then true
    else if x > bound then go (stage + 1) 2 (fuel - 1)
    else
      bndlift_coherent_pointwise x stage &&
      go stage (x + 1) (fuel - 1)
  termination_by fuel
```
