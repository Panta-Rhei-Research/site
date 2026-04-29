---
{
  "projection_kind": "taulib_declaration",
  "title": "char_pullback_true",
  "permalink": "/verify/taulib/docs/book-i-topos-earned-topos/char-pullback-true/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.EarnedTopos`.",
  "declaration_id": "TauLib.BookI.Topos.EarnedTopos::char_pullback_true",
  "declaration_slug": "char-pullback-true",
  "kind": "theorem",
  "name": "char_pullback_true",
  "module_name": "TauLib.BookI.Topos.EarnedTopos",
  "module_url": "/verify/taulib/docs/book-i-topos-earned-topos/",
  "source_line_start": 112,
  "source_line_end": 120,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L112-L120",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.EarnedTopos",
        "url": "/verify/taulib/docs/book-i-topos-earned-topos/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L112-L120",
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

- Module: [TauLib.BookI.Topos.EarnedTopos](/verify/taulib/docs/book-i-topos-earned-topos/)
- Source path: [`TauLib/BookI/Topos/EarnedTopos.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L112-L120)
- Source range: L112-L120
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The pullback of true along χ recovers the subobject:
    χ(x) = T iff both sectors confirm. -/
```

## Source Excerpt

```lean
theorem char_pullback_true (b_mem c_mem : TauIdx → Bool) (x : TauIdx) :
    characteristic_morphism b_mem c_mem x = T ↔
    b_mem x = true ∧ c_mem x = true := by
  constructor
  · intro h
    simp [characteristic_morphism, Truth4.fromBoolPair] at h
    cases hb : b_mem x <;> cases hc : c_mem x <;> simp_all
  · intro ⟨hb, hc⟩
    exact char_both_true b_mem c_mem x hb hc
```
