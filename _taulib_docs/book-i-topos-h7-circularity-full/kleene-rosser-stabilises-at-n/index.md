---
{
  "projection_kind": "taulib_declaration",
  "title": "kleene_rosser_stabilises_at_N",
  "permalink": "/verify/taulib/docs/book-i-topos-h7-circularity-full/kleene-rosser-stabilises-at-n/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H7CircularityFull`.",
  "declaration_id": "TauLib.BookI.Topos.H7CircularityFull::kleene_rosser_stabilises_at_N",
  "declaration_slug": "kleene-rosser-stabilises-at-n",
  "kind": "theorem",
  "name": "kleene_rosser_stabilises_at_N",
  "module_name": "TauLib.BookI.Topos.H7CircularityFull",
  "module_url": "/verify/taulib/docs/book-i-topos-h7-circularity-full/",
  "source_line_start": 114,
  "source_line_end": 145,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7CircularityFull.lean#L114-L145",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.H7CircularityFull",
        "url": "/verify/taulib/docs/book-i-topos-h7-circularity-full/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7CircularityFull.lean#L114-L145",
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

- Module: [TauLib.BookI.Topos.H7CircularityFull](/verify/taulib/docs/book-i-topos-h7-circularity-full/)
- Source path: [`TauLib/BookI/Topos/H7CircularityFull.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7CircularityFull.lean#L114-L145)
- Source range: L114-L145
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §7 Thm `kleene-rosser` — KR stabilises at N**.

    For any seed s, the Kleene-Rosser template's Cauchy iteration
    stabilises at N from index 1 onward. -/
```

## Source Excerpt

```lean
theorem kleene_rosser_stabilises_at_N (s : Truth4) :
    StabilisedValue kleeneRosserTemplate s N := by
  apply StabilisedValue.of_nonstab
  · -- ¬ EventuallyConst Φ s T
    intro ⟨n0, hT⟩
    have hge : max n0 1 ≥ 1 := le_max_right _ _
    have hn0 : n0 ≤ max n0 1 := le_max_left _ _
    have h1 := hT (max n0 1) hn0
    have h2 : cauchyIter kleeneRosserTemplate (max n0 1) s = N := by
      obtain ⟨k, hk⟩ : ∃ k, max n0 1 = k + 1 := ⟨max n0 1 - 1, by omega⟩
      rw [hk]; exact kleene_rosser_iter_N k s
    rw [h2] at h1; exact Truth4.noConfusion h1
  · -- ¬ EventuallyConst Φ s F
    intro ⟨n0, hF⟩
    have hge : max n0 1 ≥ 1 := le_max_right _ _
    have hn0 : n0 ≤ max n0 1 := le_max_left _ _
    have h1 := hF (max n0 1) hn0
    have h2 : cauchyIter kleeneRosserTemplate (max n0 1) s = N := by
      obtain ⟨k, hk⟩ : ∃ k, max n0 1 = k + 1 := ⟨max n0 1 - 1, by omega⟩
      rw [hk]; exact kleene_rosser_iter_N k s
    rw [h2] at h1; exact Truth4.noConfusion h1
  · -- ¬ Period2OnLobes Φ s
    intro hper
    obtain ⟨n0, h⟩ := hper
    -- Specialize at index n0 + 1 (which is ≥ n0 and ≥ 1)
    have h1 := h (n0 + 1) (Nat.le_succ n0)
    -- At index n0+1 the value is N (since n0+1 ≥ 1)
    have hN1 : cauchyIter kleeneRosserTemplate (n0 + 1) s = N :=
      kleene_rosser_iter_N n0 s
    rcases h1 with ⟨ha, _⟩ | ⟨ha, _⟩
    · rw [hN1] at ha; exact Truth4.noConfusion ha
    · rw [hN1] at ha; exact Truth4.noConfusion ha
```
