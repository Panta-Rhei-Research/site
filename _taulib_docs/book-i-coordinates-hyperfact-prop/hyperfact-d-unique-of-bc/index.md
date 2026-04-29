---
{
  "projection_kind": "taulib_declaration",
  "title": "hyperfact_D_unique_of_BC",
  "permalink": "/verify/taulib/docs/book-i-coordinates-hyperfact-prop/hyperfact-d-unique-of-bc/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.HyperfactProp`.",
  "declaration_id": "TauLib.BookI.Coordinates.HyperfactProp::hyperfact_D_unique_of_BC",
  "declaration_slug": "hyperfact-d-unique-of-bc",
  "kind": "theorem",
  "name": "hyperfact_D_unique_of_BC",
  "module_name": "TauLib.BookI.Coordinates.HyperfactProp",
  "module_url": "/verify/taulib/docs/book-i-coordinates-hyperfact-prop/",
  "source_line_start": 108,
  "source_line_end": 114,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactProp.lean#L108-L114",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.HyperfactProp",
        "url": "/verify/taulib/docs/book-i-coordinates-hyperfact-prop/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactProp.lean#L108-L114",
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

- Module: [TauLib.BookI.Coordinates.HyperfactProp](/verify/taulib/docs/book-i-coordinates-hyperfact-prop/)
- Source path: [`TauLib/BookI/Coordinates/HyperfactProp.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactProp.lean#L108-L114)
- Source range: L108-L114
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **D uniqueness**: once (a, b, c) are pinned down, the value of
    `d` is forced by the `ValidABCD` equation `tower_atom a b c · d = x`. -/
```

## Source Excerpt

```lean
theorem hyperfact_D_unique_of_BC (x a b c d₁ d₂ v : TauIdx)
    (h₁ : IsHyperfactWitness x a b c d₁ v)
    (h₂ : IsHyperfactWitness x a b c d₂ v) :
    tower_atom a b c * d₁ = tower_atom a b c * d₂ := by
  obtain ⟨⟨_, _, _, h_eq₁, _⟩, _⟩ := h₁
  obtain ⟨⟨_, _, _, h_eq₂, _⟩, _⟩ := h₂
  rw [h_eq₁, h_eq₂]
```
