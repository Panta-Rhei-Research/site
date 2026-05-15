---
{
  "projection_kind": "taulib_declaration",
  "title": "ihom_p_true_q_false",
  "permalink": "/corpus/taulib/docs/book-i-topos-internal-hom/ihom-p-true-q-false/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.InternalHom`.",
  "declaration_id": "TauLib.BookI.Topos.InternalHom::ihom_p_true_q_false",
  "declaration_slug": "ihom-p-true-q-false",
  "kind": "theorem",
  "name": "ihom_p_true_q_false",
  "module_name": "TauLib.BookI.Topos.InternalHom",
  "module_url": "/corpus/taulib/docs/book-i-topos-internal-hom/",
  "source_line_start": 50,
  "source_line_end": 53,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/InternalHom.lean#L50-L53",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.InternalHom",
        "url": "/corpus/taulib/docs/book-i-topos-internal-hom/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/InternalHom.lean#L50-L53",
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

- Module: [TauLib.BookI.Topos.InternalHom](/corpus/taulib/docs/book-i-topos-internal-hom/)
- Source path: [`TauLib/BookI/Topos/InternalHom.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/InternalHom.lean#L50-L53)
- Source range: L50-L53
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Internal hom evaluates correctly when P holds but Q fails. -/
```

## Source Excerpt

```lean
theorem ihom_p_true_q_false (P Q : Presheaf) (x : TauIdx)
    (hp : P.support x = true) (hq : Q.support x = false) :
    (internal_hom P Q).support x = false := by
  simp [internal_hom, hp, hq]
```
