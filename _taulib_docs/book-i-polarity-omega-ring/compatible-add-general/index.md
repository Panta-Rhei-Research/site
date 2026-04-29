---
{
  "projection_kind": "taulib_declaration",
  "title": "Compatible_add_general",
  "permalink": "/verify/taulib/docs/book-i-polarity-omega-ring/compatible-add-general/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.OmegaRing`.",
  "declaration_id": "TauLib.BookI.Polarity.OmegaRing::Compatible_add_general",
  "declaration_slug": "compatible-add-general",
  "kind": "theorem",
  "name": "Compatible_add_general",
  "module_name": "TauLib.BookI.Polarity.OmegaRing",
  "module_url": "/verify/taulib/docs/book-i-polarity-omega-ring/",
  "source_line_start": 168,
  "source_line_end": 186,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaRing.lean#L168-L186",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.OmegaRing",
        "url": "/verify/taulib/docs/book-i-polarity-omega-ring/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaRing.lean#L168-L186",
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

- Module: [TauLib.BookI.Polarity.OmegaRing](/verify/taulib/docs/book-i-polarity-omega-ring/)
- Source path: [`TauLib/BookI/Polarity/OmegaRing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaRing.lean#L168-L186)
- Source range: L168-L186
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- General compatibility preservation under addition. -/
```

## Source Excerpt

```lean
theorem Compatible_add_general (t1 t2 : OmegaTail) (hd : t1.depth = t2.depth)
    (h1 : Compatible t1) (h2 : Compatible t2) :
    Compatible (t1.add t2 hd) := by
  intro k l hk hkl hld
  have hdepth : (t1.add t2 hd).depth = t1.depth := by simp [OmegaTail.add]
  have hld' : l ≤ t1.depth := by rw [← hdepth]; exact hld
  have hl : l - 1 < t1.depth := by simp only [TauIdx] at *; omega
  have hk' : k - 1 < t1.depth := by simp only [TauIdx] at *; omega
  have hl1 : l - 1 + 1 = l := by simp only [TauIdx] at *; omega
  have hk1 : k - 1 + 1 = k := by simp only [TauIdx] at *; omega
  rw [add_getD t1 t2 hd (l - 1) hl, add_getD t1 t2 hd (k - 1) hk']
  -- Normalize: primorial (l-1+1) → primorial l, primorial (k-1+1) → primorial k
  rw [hl1, hk1]
  -- Goal: ((x_l + y_l) % M_l) % M_k = (x_k + y_k) % M_k
  rw [mod_mod_of_dvd _ _ _ (primorial_dvd hkl)]
  -- Goal: (x_l + y_l) % M_k = (x_k + y_k) % M_k
  rw [Nat.add_mod (t1.components.getD (l-1) 0) (t2.components.getD (l-1) 0) (primorial k)]
  -- Goal: ((x_l % M_k) + (y_l % M_k)) % M_k = (x_k + y_k) % M_k
  rw [h1 k l hk hkl hld', h2 k l hk hkl (by rw [← hd]; exact hld')]
```
