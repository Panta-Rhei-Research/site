---
{
  "projection_kind": "taulib_declaration",
  "title": "normal_hierarchy_is_theorem",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-neutrino-background/normal-hierarchy-is-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.NeutrinoBackground`.",
  "declaration_id": "TauLib.BookV.Cosmology.NeutrinoBackground::normal_hierarchy_is_theorem",
  "declaration_slug": "normal-hierarchy-is-theorem",
  "kind": "theorem",
  "name": "normal_hierarchy_is_theorem",
  "module_name": "TauLib.BookV.Cosmology.NeutrinoBackground",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-neutrino-background/",
  "source_line_start": 187,
  "source_line_end": 189,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L187-L189",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NeutrinoBackground",
        "url": "/corpus/taulib/docs/book-v-cosmology-neutrino-background/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L187-L189",
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

- Module: [TauLib.BookV.Cosmology.NeutrinoBackground](/corpus/taulib/docs/book-v-cosmology-neutrino-background/)
- Source path: [`TauLib/BookV/Cosmology/NeutrinoBackground.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L187-L189)
- Source range: L187-L189
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Normal ordering is a theorem: all spacings positive → m₁ < m₂ < m₃.
    Verified as Nat comparisons (203 > 0, 609 > 0, 1421 > 0). -/
```

## Source Excerpt

```lean
theorem normal_hierarchy_is_theorem :
    (203 : Nat) > 0 ∧ (609 : Nat) > 0 ∧ (1421 : Nat) > 0 :=
  ⟨by omega, by omega, by omega⟩
```
