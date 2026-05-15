---
{
  "projection_kind": "taulib_declaration",
  "title": "neutrino_43_counting",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-43-counting/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::neutrino_43_counting",
  "declaration_slug": "neutrino-43-counting",
  "kind": "theorem",
  "name": "neutrino_43_counting",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 689,
  "source_line_end": 690,
  "registry_ids": [
    "V.T178"
  ],
  "related_registry_items": [
    {
      "id": "V.T178",
      "title": "Structural Derivation: Δpq/Δpr = 4/3 from Lemniscate Counting",
      "url": "/registry/object/V.T178/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L689-L690",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
        "url": "/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L689-L690",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L689-L690)
- Source range: L689-L690
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `V.T178` — Structural Derivation: Δpq/Δpr = 4/3 from Lemniscate Counting

## Immediate Comment / Docstring

```lean
-- [V.T178] Structural arithmetic checks (exact)
```

## Source Excerpt

```lean
theorem neutrino_43_counting :
    (2 * 2 : Nat) = 4 ∧ (4 : Nat) + 3 = 7 := ⟨by rfl, by rfl⟩
```
