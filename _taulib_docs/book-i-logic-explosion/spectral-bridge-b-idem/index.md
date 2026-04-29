---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_bridge_B_idem",
  "permalink": "/verify/taulib/docs/book-i-logic-explosion/spectral-bridge-b-idem/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Logic.Explosion`.",
  "declaration_id": "TauLib.BookI.Logic.Explosion::spectral_bridge_B_idem",
  "declaration_slug": "spectral-bridge-b-idem",
  "kind": "theorem",
  "name": "spectral_bridge_B_idem",
  "module_name": "TauLib.BookI.Logic.Explosion",
  "module_url": "/verify/taulib/docs/book-i-logic-explosion/",
  "source_line_start": 168,
  "source_line_end": 173,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Explosion.lean#L168-L173",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Logic.Explosion",
        "url": "/verify/taulib/docs/book-i-logic-explosion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Explosion.lean#L168-L173",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Logic.Explosion](/verify/taulib/docs/book-i-logic-explosion/)
- Source path: [`TauLib/BookI/Logic/Explosion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Explosion.lean#L168-L173)
- Source range: L168-L173
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The sector product of B with itself is B (idempotent), matching e+^2 = e+. -/
```

## Source Excerpt

```lean
theorem spectral_bridge_B_idem :
    Tau.Polarity.SectorPair.mul
      (Truth4.toSectorPair B) (Truth4.toSectorPair B) =
    Truth4.toSectorPair B := by
  simp [Truth4.toSectorPair, Tau.Polarity.e_plus_sector,
        Tau.Polarity.SectorPair.mul]
```
