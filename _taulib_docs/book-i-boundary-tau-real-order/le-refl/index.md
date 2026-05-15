---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.le_refl",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-real-order/le-refl/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealOrder`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealOrder::TauReal.le_refl",
  "declaration_slug": "le-refl",
  "kind": "theorem",
  "name": "TauReal.le_refl",
  "module_name": "TauLib.BookI.Boundary.TauRealOrder",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-real-order/",
  "source_line_start": 110,
  "source_line_end": 121,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L110-L121",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealOrder",
        "url": "/corpus/taulib/docs/book-i-boundary-tau-real-order/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L110-L121",
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

- Module: [TauLib.BookI.Boundary.TauRealOrder](/corpus/taulib/docs/book-i-boundary-tau-real-order/)
- Source path: [`TauLib/BookI/Boundary/TauRealOrder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L110-L121)
- Source range: L110-L121
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `le` is reflexive. -/
```

## Source Excerpt

```lean
theorem TauReal.le_refl (a : TauReal) : TauReal.le a a := by
  intro k
  refine ⟨0, fun n _ => ?_⟩
  unfold TauRat.lt
  rw [toRat_add, TauRat.ofNatRecip_toRat]
  -- Goal: (a.approx n).toRat < (a.approx n).toRat + 1 / (k + 1)
  have h_pos : (0 : Rat) < 1 / ((k : Rat) + 1) := by
    have : (0 : Rat) < (k : Rat) + 1 := by
      have : (0 : Rat) ≤ (k : Rat) := by exact_mod_cast Nat.zero_le k
      linarith
    exact div_pos (by norm_num) this
  linarith
```
