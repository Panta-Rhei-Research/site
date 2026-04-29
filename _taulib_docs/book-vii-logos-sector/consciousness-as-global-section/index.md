---
{
  "projection_kind": "taulib_declaration",
  "title": "consciousness_as_global_section",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/consciousness-as-global-section/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::consciousness_as_global_section",
  "declaration_slug": "consciousness-as-global-section",
  "kind": "theorem",
  "name": "consciousness_as_global_section",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 158,
  "source_line_end": 161,
  "registry_ids": [
    "VII.T41"
  ],
  "related_registry_items": [
    {
      "id": "VII.T41",
      "title": "Consciousness as Global Section",
      "url": "/registry/object/VII.T41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L158-L161",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Logos.Sector",
        "url": "/verify/taulib/docs/book-vii-logos-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L158-L161",
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

- Module: [TauLib.BookVII.Logos.Sector](/verify/taulib/docs/book-vii-logos-sector/)
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L158-L161)
- Source range: L158-L161
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T41` — Consciousness as Global Section

## Immediate Comment / Docstring

```lean
/-- [VII.T41] Consciousness as Global Section (ch108). Consciousness
    modelled as a global section of the mind-topos presheaf:
    Γ(Mind) = global assignment of mental content compatible with
    all transitions. Consciousness exists iff the sheaf condition
    holds (local mental states glue globally). -/
```

## Source Excerpt

```lean
theorem consciousness_as_global_section :
    mind_topos.topos_structure = true ∧
    mind_topos.has_internal_logic = true :=
  ⟨rfl, rfl⟩
```
