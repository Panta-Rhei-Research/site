---
{
  "projection_kind": "taulib_declaration",
  "title": "kripke_soundness",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/kripke-soundness/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::kripke_soundness",
  "declaration_slug": "kripke-soundness",
  "kind": "theorem",
  "name": "kripke_soundness",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 834,
  "source_line_end": 840,
  "registry_ids": [
    "VII.T28"
  ],
  "related_registry_items": [
    {
      "id": "VII.T28",
      "title": "Kripke Soundness in τ",
      "url": "/registry/object/VII.T28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L834-L840",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/verify/taulib/docs/book-vii-ethics-ciproof/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L834-L840",
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L834-L840)
- Source range: L834-L840
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T28` — Kripke Soundness in τ

## Immediate Comment / Docstring

```lean
/-- [VII.T28] Kripke Soundness in τ (ch43). The internal modal
    frame satisfies S4 axioms. Soundness: if □φ holds at w, then
    φ holds at all accessible w'. Completeness relative to S4.
    The modal operators from VII.D33 are sound w.r.t. this frame. -/
```

## Source Excerpt

```lean
theorem kripke_soundness :
    modal_frame.worlds_as_addresses = true ∧
    modal_frame.accessibility_admissible = true ∧
    modal_frame.internal = true ∧
    accessibility.reflexive = true ∧
    accessibility.transitive = true :=
  ⟨rfl, rfl, rfl, rfl, rfl⟩
```
