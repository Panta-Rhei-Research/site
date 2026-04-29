---
{
  "projection_kind": "taulib_declaration",
  "title": "unique_mixing_pair",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewmixing/unique-mixing-pair/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.EWMixing`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWMixing::unique_mixing_pair",
  "declaration_slug": "unique-mixing-pair",
  "kind": "theorem",
  "name": "unique_mixing_pair",
  "module_name": "TauLib.BookIV.Electroweak.EWMixing",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/",
  "source_line_start": 318,
  "source_line_end": 320,
  "registry_ids": [
    "IV.T62"
  ],
  "related_registry_items": [
    {
      "id": "IV.T62",
      "title": "Mixing Uniqueness Theorem",
      "url": "/registry/object/IV.T62/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L318-L320",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWMixing",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L318-L320",
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

- Module: [TauLib.BookIV.Electroweak.EWMixing](/verify/taulib/docs/book-iv-electroweak-ewmixing/)
- Source path: [`TauLib/BookIV/Electroweak/EWMixing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L318-L320)
- Source range: L318-L320
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T62` — Mixing Uniqueness Theorem

## Immediate Comment / Docstring

```lean
/-- [IV.T62] (A,B) is the unique mixing-compatible sector pair.

    Proof sketch:
    - A is the unique balanced-polarity sector (IV.D06).
    - B is the unique χ₊-dominant fiber sector (IV.D02).
    - No other pair satisfies both mixing conditions simultaneously.
    - D is χ₊-dominant but lives on the BASE, not the fiber.
    - C is χ₋-dominant (wrong polarity for photon emergence).
    - Ω is crossing (neither balanced nor purely χ₊). -/
```

## Source Excerpt

```lean
theorem unique_mixing_pair :
    mixing_pair.balanced = .A ∧ mixing_pair.chi_plus_fiber = .B :=
  ⟨mixing_pair.balanced_is_A, mixing_pair.chi_plus_is_B⟩
```
