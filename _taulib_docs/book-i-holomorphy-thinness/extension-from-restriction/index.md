---
{
  "projection_kind": "taulib_declaration",
  "title": "extension_from_restriction",
  "permalink": "/corpus/taulib/docs/book-i-holomorphy-thinness/extension-from-restriction/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.Thinness`.",
  "declaration_id": "TauLib.BookI.Holomorphy.Thinness::extension_from_restriction",
  "declaration_slug": "extension-from-restriction",
  "kind": "theorem",
  "name": "extension_from_restriction",
  "module_name": "TauLib.BookI.Holomorphy.Thinness",
  "module_url": "/corpus/taulib/docs/book-i-holomorphy-thinness/",
  "source_line_start": 124,
  "source_line_end": 128,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/Thinness.lean#L124-L128",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.Thinness",
        "url": "/corpus/taulib/docs/book-i-holomorphy-thinness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/Thinness.lean#L124-L128",
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

- Module: [TauLib.BookI.Holomorphy.Thinness](/corpus/taulib/docs/book-i-holomorphy-thinness/)
- Source path: [`TauLib/BookI/Holomorphy/Thinness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/Thinness.lean#L124-L128)
- Source range: L124-L128
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Extension from restriction: if f₁ restricted to inputs NOT in K
    equals f₂ restricted to inputs NOT in K, and both are tower-coherent
    with agreement at some depth, then they agree everywhere. -/
```

## Source Excerpt

```lean
theorem extension_from_restriction (f₁ f₂ : StageFun)
    (hcoh1 : TowerCoherent f₁) (hcoh2 : TowerCoherent f₂)
    (d₀ : TauIdx) (hagree_d0 : ∀ n, agree_at f₁ f₂ n d₀) :
    ∀ n k, k ≤ d₀ → f₁.b_fun n k = f₂.b_fun n k :=
  fun n k hk => (removable_singularity f₁ f₂ hcoh1 hcoh2 d₀ hagree_d0 n k hk).1
```
