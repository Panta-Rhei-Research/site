---
{
  "projection_kind": "taulib_declaration",
  "title": "EarnedTopos",
  "permalink": "/verify/taulib/docs/book-i-topos-earned-topos/earned-topos/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Topos.EarnedTopos`.",
  "declaration_id": "TauLib.BookI.Topos.EarnedTopos::EarnedTopos",
  "declaration_slug": "earned-topos",
  "kind": "structure",
  "name": "EarnedTopos",
  "module_name": "TauLib.BookI.Topos.EarnedTopos",
  "module_url": "/verify/taulib/docs/book-i-topos-earned-topos/",
  "source_line_start": 128,
  "source_line_end": 134,
  "registry_ids": [
    "I.D59"
  ],
  "related_registry_items": [
    {
      "id": "I.D59",
      "title": "Earned Topos",
      "url": "/registry/object/I.D59/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L128-L134",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.EarnedTopos",
        "url": "/verify/taulib/docs/book-i-topos-earned-topos/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L128-L134",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookI.Topos.EarnedTopos](/verify/taulib/docs/book-i-topos-earned-topos/)
- Source path: [`TauLib/BookI/Topos/EarnedTopos.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L128-L134)
- Source range: L128-L134
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D59` — Earned Topos

## Immediate Comment / Docstring

```lean
/-- [I.D59] The earned topos E_τ = PSh(Cat_τ) with Ω_τ as subobject classifier.
    Bundles the Grothendieck topos structure with the four-valued classifier. -/
```

## Source Excerpt

```lean
structure EarnedTopos where
  /-- The underlying presheaf topos. -/
  topos : PShCatTau := ⟨⟨fun _ => true⟩⟩
  /-- The subobject classifier is Truth4. -/
  classifier : Type := Omega_tau
  /-- The "true" arrow. -/
  true_arrow : Omega_tau := omega_true
```
