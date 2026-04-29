---
{
  "projection_kind": "taulib_declaration",
  "title": "central_theorem_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/central-theorem-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.CentralTheorem`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.CentralTheorem::central_theorem_check",
  "declaration_slug": "central-theorem-check",
  "kind": "def",
  "name": "central_theorem_check",
  "module_name": "TauLib.BookII.CentralTheorem.CentralTheorem",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/",
  "source_line_start": 270,
  "source_line_end": 280,
  "registry_ids": [
    "II.T40"
  ],
  "related_registry_items": [
    {
      "id": "II.T40",
      "title": "Central Theorem",
      "url": "/registry/object/II.T40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L270-L280",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.CentralTheorem",
        "url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L270-L280",
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

- Module: [TauLib.BookII.CentralTheorem.CentralTheorem](/verify/taulib/docs/book-ii-central-theorem-central-theorem/)
- Source path: [`TauLib/BookII/CentralTheorem/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L270-L280)
- Source range: L270-L280
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T40` — Central Theorem

## Immediate Comment / Docstring

```lean
/-- [II.T40] THE CENTRAL THEOREM CHECK.
    Combines all four links of the isomorphism:
    1. Spectral algebra ring structure (II.D60)
    2. Forward direction: boundary -> holomorphic (II.T37-T38)
    3. Inverse direction: holomorphic -> boundary (II.T39, II.T33)
    4. Round-trip: both compositions are identity

    This is THE main verification of Book II. -/
```

## Source Excerpt

```lean
def central_theorem_check (db bound : TauIdx) : Bool :=
  -- Ring structure of spectral algebra
  spectral_algebra_stage_ring_check db bound &&
  -- Tower structure of spectral algebra
  spectral_algebra_tower_check db bound &&
  -- Forward: boundary -> holomorphic
  central_theorem_forward_check db bound &&
  -- Inverse: holomorphic -> boundary
  central_theorem_inverse_check db bound &&
  -- Round-trip: isomorphism verification
  central_theorem_roundtrip_check db bound
```
