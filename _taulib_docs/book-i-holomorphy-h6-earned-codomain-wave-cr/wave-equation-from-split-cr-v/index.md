---
{
  "projection_kind": "taulib_declaration",
  "title": "wave_equation_from_split_cr_v",
  "permalink": "/corpus/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/wave-equation-from-split-cr-v/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR::wave_equation_from_split_cr_v",
  "declaration_slug": "wave-equation-from-split-cr-v",
  "kind": "theorem",
  "name": "wave_equation_from_split_cr_v",
  "module_name": "TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR",
  "module_url": "/corpus/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/",
  "source_line_start": 227,
  "source_line_end": 234,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L227-L234",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR",
        "url": "/corpus/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L227-L234",
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

- Module: [TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR](/corpus/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/)
- Source path: [`TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L227-L234)
- Source range: L227-L234
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §5 wave equation for v-component (companion theorem)**.

    By symmetry of the CR system: the v-component also satisfies
    the wave equation `∂_t² v = ∂_x² v`. -/
```

## Source Excerpt

```lean
theorem wave_equation_from_split_cr_v {α : Type*}
    (dt dx : (α → Int) → (α → Int))
    (commute : ∀ f, dt (dx f) = dx (dt f))
    (u v : α → Int)
    (cr : split_cr_system dt dx u v) :
    dt (dt v) = dx (dx v) := by
  obtain ⟨cr1, cr2⟩ := cr
  rw [← cr2, commute, cr1]
```
