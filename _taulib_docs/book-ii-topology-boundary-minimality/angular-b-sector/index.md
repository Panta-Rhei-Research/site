---
{
  "projection_kind": "taulib_declaration",
  "title": "angular_b_sector",
  "permalink": "/verify/taulib/docs/book-ii-topology-boundary-minimality/angular-b-sector/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.BoundaryMinimality`.",
  "declaration_id": "TauLib.BookII.Topology.BoundaryMinimality::angular_b_sector",
  "declaration_slug": "angular-b-sector",
  "kind": "def",
  "name": "angular_b_sector",
  "module_name": "TauLib.BookII.Topology.BoundaryMinimality",
  "module_url": "/verify/taulib/docs/book-ii-topology-boundary-minimality/",
  "source_line_start": 39,
  "source_line_end": 41,
  "registry_ids": [
    "II.D17"
  ],
  "related_registry_items": [
    {
      "id": "II.D17",
      "title": "Angular Sectors",
      "url": "/registry/object/II.D17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/BoundaryMinimality.lean#L39-L41",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Topology.BoundaryMinimality",
        "url": "/verify/taulib/docs/book-ii-topology-boundary-minimality/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/BoundaryMinimality.lean#L39-L41",
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

- Module: [TauLib.BookII.Topology.BoundaryMinimality](/verify/taulib/docs/book-ii-topology-boundary-minimality/)
- Source path: [`TauLib/BookII/Topology/BoundaryMinimality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/BoundaryMinimality.lean#L39-L41)
- Source range: L39-L41
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D17` — Angular Sectors

## Immediate Comment / Docstring

```lean
/-- [II.D17] B-angular sector at stage k:
    points with B-coordinate ≡ b (mod p_k). -/
```

## Source Excerpt

```lean
def angular_b_sector (x k : TauIdx) : TauIdx :=
  let p := from_tau_idx x
  p.b % nth_prime k
```
