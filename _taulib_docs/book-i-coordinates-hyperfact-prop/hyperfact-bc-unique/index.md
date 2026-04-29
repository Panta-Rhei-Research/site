---
{
  "projection_kind": "taulib_declaration",
  "title": "hyperfact_BC_unique",
  "permalink": "/verify/taulib/docs/book-i-coordinates-hyperfact-prop/hyperfact-bc-unique/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.HyperfactProp`.",
  "declaration_id": "TauLib.BookI.Coordinates.HyperfactProp::hyperfact_BC_unique",
  "declaration_slug": "hyperfact-bc-unique",
  "kind": "theorem",
  "name": "hyperfact_BC_unique",
  "module_name": "TauLib.BookI.Coordinates.HyperfactProp",
  "module_url": "/verify/taulib/docs/book-i-coordinates-hyperfact-prop/",
  "source_line_start": 85,
  "source_line_end": 100,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactProp.lean#L85-L100",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactProp.lean#L85-L100",
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
- Source path: [`TauLib/BookI/Coordinates/HyperfactProp.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactProp.lean#L85-L100)
- Source range: L85-L100
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **(B, C) uniqueness** for hyperfactorization given a fixed (x, a, v):
    if two witnesses share the same `a` and v-form valuation `v`,
    their `(b, c)` pairs agree.  Direct application of `no_tie`. -/
```

## Source Excerpt

```lean
theorem hyperfact_BC_unique (x a v b₁ c₁ d₁ b₂ c₂ d₂ : TauIdx)
    (h₁ : IsHyperfactWitness x a b₁ c₁ d₁ v)
    (h₂ : IsHyperfactWitness x a b₂ c₂ d₂ v) :
    c₁ = c₂ ∧ b₁ = b₂ := by
  obtain ⟨⟨ha, hb₁_pos, hc₁_pos, _, _⟩, hv₁, hmax₁⟩ := h₁
  obtain ⟨⟨_, hb₂_pos, hc₂_pos, _, _⟩, hv₂, hmax₂⟩ := h₂
  -- v-form equality: b₁ · A↑↑(c₁-1) = v = b₂ · A↑↑(c₂-1)
  have h_v_eq : b₁ * tetration a (c₁ - 1) = b₂ * tetration a (c₂ - 1) := by
    rw [hv₁, ← hv₂]
  -- Maximality: ¬ (A↑↑c ∣ b · A↑↑(c-1))  for both witnesses
  have hmax₁' : ¬ (tetration a c₁ ∣ b₁ * tetration a (c₁ - 1)) := by
    rw [hv₁]; exact hmax₁
  have hmax₂' : ¬ (tetration a c₂ ∣ b₂ * tetration a (c₂ - 1)) := by
    rw [hv₂]; exact hmax₂
  exact no_tie a b₁ c₁ b₂ c₂ ha hb₁_pos hc₁_pos hb₂_pos hc₂_pos
    h_v_eq hmax₁' hmax₂'
```
