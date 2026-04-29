---
{
  "projection_kind": "taulib_declaration",
  "title": "overlap_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/overlap-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.SheafCoherence`.",
  "declaration_id": "TauLib.BookII.Hartogs.SheafCoherence::overlap_check",
  "declaration_slug": "overlap-check",
  "kind": "def",
  "name": "overlap_check",
  "module_name": "TauLib.BookII.Hartogs.SheafCoherence",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/",
  "source_line_start": 151,
  "source_line_end": 163,
  "registry_ids": [
    "II.L06"
  ],
  "related_registry_items": [
    {
      "id": "II.L06",
      "title": "Gluing Lemma",
      "url": "/registry/object/II.L06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L151-L163",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.SheafCoherence",
        "url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L151-L163",
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

- Module: [TauLib.BookII.Hartogs.SheafCoherence](/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/)
- Source path: [`TauLib/BookII/Hartogs/SheafCoherence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L151-L163)
- Source range: L151-L163
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L06` — Gluing Lemma

## Immediate Comment / Docstring

```lean
/-- [II.L06] Same-stage overlap check:
    For a ≠ b, the cylinders C_{k,a} and C_{k,b} are disjoint.
    This is the ultrametric property: same-stage cylinders do not overlap.

    Returns true iff no x in [0, P_k) belongs to both C_{k,a} and C_{k,b}. -/
```

## Source Excerpt

```lean
def overlap_check (k a b : TauIdx) : Bool :=
  if a == b then true  -- same cylinder, trivially "compatible"
  else go 0 (primorial k) k a b
where
  go (x fuel k a b : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= primorial k then true
    else
      -- x cannot be in both C_{k,a} and C_{k,b}
      let in_a := presheaf_assign k a x
      let in_b := presheaf_assign k b x
      (!(in_a && in_b)) && go (x + 1) (fuel - 1) k a b
  termination_by fuel
```
