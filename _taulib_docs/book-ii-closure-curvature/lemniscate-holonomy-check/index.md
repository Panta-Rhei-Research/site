---
{
  "projection_kind": "taulib_declaration",
  "title": "lemniscate_holonomy_check",
  "permalink": "/verify/taulib/docs/book-ii-closure-curvature/lemniscate-holonomy-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.Curvature`.",
  "declaration_id": "TauLib.BookII.Closure.Curvature::lemniscate_holonomy_check",
  "declaration_slug": "lemniscate-holonomy-check",
  "kind": "def",
  "name": "lemniscate_holonomy_check",
  "module_name": "TauLib.BookII.Closure.Curvature",
  "module_url": "/verify/taulib/docs/book-ii-closure-curvature/",
  "source_line_start": 145,
  "source_line_end": 158,
  "registry_ids": [
    "II.T52"
  ],
  "related_registry_items": [
    {
      "id": "II.T52",
      "title": "Lemniscate Holonomy",
      "url": "/registry/object/II.T52/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L145-L158",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.Curvature",
        "url": "/verify/taulib/docs/book-ii-closure-curvature/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L145-L158",
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

- Module: [TauLib.BookII.Closure.Curvature](/verify/taulib/docs/book-ii-closure-curvature/)
- Source path: [`TauLib/BookII/Closure/Curvature.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L145-L158)
- Source range: L145-L158
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T52` — Lemniscate Holonomy

## Immediate Comment / Docstring

```lean
/-- [II.T52] The lemniscate L = S¹ ∨ S¹ has π₁(L) ≅ ℤ (free group on 1 gen).
    The holonomy representation maps the generator to a "rotation" in the
    fiber T². At stage k, this is the shift x ↦ x+1 mod M_k.

    Check: the generator of the holonomy is the unit shift. -/
```

## Source Excerpt

```lean
def lemniscate_holonomy_check (k : Nat) : Bool :=
  let pk := primorial k
  -- The shift by 1 has order pk (returns to start after pk steps)
  let shifted := go 0 1 pk pk
  shifted == pk
where
  -- Count steps until we return to 0
  go (pos step pk fuel : Nat) : Nat :=
    if fuel = 0 then 0
    else
      let next := (pos + 1) % pk
      if next == 0 && step > 0 then step
      else go next (step + 1) pk (fuel - 1)
  termination_by fuel
```
