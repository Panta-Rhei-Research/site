---
{
  "projection_kind": "taulib_declaration",
  "title": "fermi_low_energy",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/fermi-low-energy/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy2::fermi_low_energy",
  "declaration_slug": "fermi-low-energy",
  "kind": "def",
  "name": "fermi_low_energy",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/",
  "source_line_start": 149,
  "source_line_end": 153,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L149-L153",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy2",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L149-L153",
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy2](/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L149-L153)
- Source range: L149-L153
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Fermi theory as low-energy limit. -/
```

## Source Excerpt

```lean
def fermi_low_energy : FermiTheory where
  energy_below_mw := true
  below_true := rfl
  operator_dim := 6
  dim_eq := rfl
```
