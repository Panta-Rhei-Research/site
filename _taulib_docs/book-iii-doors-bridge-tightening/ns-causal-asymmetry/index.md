---
{
  "projection_kind": "taulib_declaration",
  "title": "ns_causal_asymmetry",
  "permalink": "/verify/taulib/docs/book-iii-doors-bridge-tightening/ns-causal-asymmetry/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.BridgeTightening`.",
  "declaration_id": "TauLib.BookIII.Doors.BridgeTightening::ns_causal_asymmetry",
  "declaration_slug": "ns-causal-asymmetry",
  "kind": "def",
  "name": "ns_causal_asymmetry",
  "module_name": "TauLib.BookIII.Doors.BridgeTightening",
  "module_url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/",
  "source_line_start": 139,
  "source_line_end": 142,
  "registry_ids": [
    "III.T62"
  ],
  "related_registry_items": [
    {
      "id": "III.T62",
      "title": "NS Flow Causal Arrow",
      "url": "/registry/object/III.T62/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L139-L142",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.BridgeTightening",
        "url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L139-L142",
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

- Module: [TauLib.BookIII.Doors.BridgeTightening](/verify/taulib/docs/book-iii-doors-bridge-tightening/)
- Source path: [`TauLib/BookIII/Doors/BridgeTightening.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L139-L142)
- Source range: L139-L142
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T62` — NS Flow Causal Arrow

## Immediate Comment / Docstring

```lean
/-- [III.T62] Causal arrow: B/C asymmetry grows with stage depth.
    The asymmetry |B_k - C_k| is positive for k ≥ 2 (lobes break
    symmetry). This generates a preferred flow direction. -/
```

## Source Excerpt

```lean
def ns_causal_asymmetry (k : Nat) : Nat :=
  let b := split_zeta_b k
  let c := split_zeta_c k
  if b >= c then b - c else c - b
```
