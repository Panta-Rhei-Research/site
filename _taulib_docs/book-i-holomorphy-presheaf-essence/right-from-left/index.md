---
{
  "projection_kind": "taulib_declaration",
  "title": "right_from_left",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/right-from-left/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.PresheafEssence`.",
  "declaration_id": "TauLib.BookI.Holomorphy.PresheafEssence::right_from_left",
  "declaration_slug": "right-from-left",
  "kind": "theorem",
  "name": "right_from_left",
  "module_name": "TauLib.BookI.Holomorphy.PresheafEssence",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/",
  "source_line_start": 160,
  "source_line_end": 170,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L160-L170",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.PresheafEssence",
        "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L160-L170",
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

- Module: [TauLib.BookI.Holomorphy.PresheafEssence](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/)
- Source path: [`TauLib/BookI/Holomorphy/PresheafEssence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L160-L170)
- Source range: L160-L170
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Key insight.** The right square (spectral naturality) follows
    automatically from the left square (tower coherence).

    Because `spectral_of f n k = ⟨f.b_fun n k, f.c_fun n k⟩`,
    spectral reduction IS sector-wise tower coherence.
    The two squares are independent in the LaTeX presentation
    but are the same condition in TauLib's concrete formulation. -/
```

## Source Excerpt

```lean
theorem right_from_left (bs : BiSquare) (n k l : TauIdx) (hkl : k ≤ l) :
    spectral_of bs.stage_fun n k =
    ⟨reduce (spectral_of bs.stage_fun n l).b_coeff k,
     reduce (spectral_of bs.stage_fun n l).c_coeff k⟩ := by
  apply spectral_coeff_ext
  · -- b_coeff: f.b(n, k) = reduce(f.b(n, l), k)
    show bs.stage_fun.b_fun n k = reduce (bs.stage_fun.b_fun n l) k
    exact (bs.left_b n k l hkl).symm
  · -- c_coeff: f.c(n, k) = reduce(f.c(n, l), k)
    show bs.stage_fun.c_fun n k = reduce (bs.stage_fun.c_fun n l) k
    exact (bs.left_c n k l hkl).symm
```
