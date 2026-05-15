---
{
  "projection_kind": "taulib_declaration",
  "title": "char_underdetermined",
  "permalink": "/corpus/taulib/docs/book-i-topos-earned-topos/char-underdetermined/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.EarnedTopos`.",
  "declaration_id": "TauLib.BookI.Topos.EarnedTopos::char_underdetermined",
  "declaration_slug": "char-underdetermined",
  "kind": "theorem",
  "name": "char_underdetermined",
  "module_name": "TauLib.BookI.Topos.EarnedTopos",
  "module_url": "/corpus/taulib/docs/book-i-topos-earned-topos/",
  "source_line_start": 105,
  "source_line_end": 108,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L105-L108",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.EarnedTopos",
        "url": "/corpus/taulib/docs/book-i-topos-earned-topos/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L105-L108",
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

- Module: [TauLib.BookI.Topos.EarnedTopos](/corpus/taulib/docs/book-i-topos-earned-topos/)
- Source path: [`TauLib/BookI/Topos/EarnedTopos.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L105-L108)
- Source range: L105-L108
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Characteristic morphism: neither confirms ⟹ N. -/
```

## Source Excerpt

```lean
theorem char_underdetermined (b_mem c_mem : TauIdx → Bool) (x : TauIdx)
    (hb : b_mem x = false) (hc : c_mem x = true) :
    characteristic_morphism b_mem c_mem x = N := by
  simp [characteristic_morphism, hb, hc, Truth4.fromBoolPair]
```
