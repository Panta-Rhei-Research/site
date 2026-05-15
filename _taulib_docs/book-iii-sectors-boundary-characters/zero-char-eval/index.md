---
{
  "projection_kind": "taulib_declaration",
  "title": "zero_char_eval",
  "permalink": "/corpus/taulib/docs/book-iii-sectors-boundary-characters/zero-char-eval/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Sectors.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookIII.Sectors.BoundaryCharacters::zero_char_eval",
  "declaration_slug": "zero-char-eval",
  "kind": "theorem",
  "name": "zero_char_eval",
  "module_name": "TauLib.BookIII.Sectors.BoundaryCharacters",
  "module_url": "/corpus/taulib/docs/book-iii-sectors-boundary-characters/",
  "source_line_start": 195,
  "source_line_end": 198,
  "registry_ids": [
    "III.D11"
  ],
  "related_registry_items": [
    {
      "id": "III.D11",
      "title": "Boundary Character Space",
      "url": "/registry/object/III.D11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L195-L198",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.BoundaryCharacters",
        "url": "/corpus/taulib/docs/book-iii-sectors-boundary-characters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L195-L198",
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

- Module: [TauLib.BookIII.Sectors.BoundaryCharacters](/corpus/taulib/docs/book-iii-sectors-boundary-characters/)
- Source path: [`TauLib/BookIII/Sectors/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L195-L198)
- Source range: L195-L198
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D11` — Boundary Character Space

## Immediate Comment / Docstring

```lean
/-- [III.D11] Structural: zero character evaluates to zero. -/
```

## Source Excerpt

```lean
theorem zero_char_eval (x k : TauIdx) :
    BoundaryCharacter.zero.eval x k = 0 := by
  simp only [BoundaryCharacter.zero, BoundaryCharacter.eval]
  ring
```
