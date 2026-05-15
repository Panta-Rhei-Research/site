---
{
  "projection_kind": "taulib_declaration",
  "title": "label_5_is_B",
  "permalink": "/corpus/taulib/docs/book-iii-doors-grand-grh/label-5-is-b/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.GrandGRH`.",
  "declaration_id": "TauLib.BookIII.Doors.GrandGRH::label_5_is_B",
  "declaration_slug": "label-5-is-b",
  "kind": "theorem",
  "name": "label_5_is_B",
  "module_name": "TauLib.BookIII.Doors.GrandGRH",
  "module_url": "/corpus/taulib/docs/book-iii-doors-grand-grh/",
  "source_line_start": 240,
  "source_line_end": 240,
  "registry_ids": [
    "III.T20"
  ],
  "related_registry_items": [
    {
      "id": "III.T20",
      "title": "Prime Polarity Scaling Theorem",
      "url": "/registry/object/III.T20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L240-L240",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.GrandGRH",
        "url": "/corpus/taulib/docs/book-iii-doors-grand-grh/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L240-L240",
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

- Module: [TauLib.BookIII.Doors.GrandGRH](/corpus/taulib/docs/book-iii-doors-grand-grh/)
- Source path: [`TauLib/BookIII/Doors/GrandGRH.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L240-L240)
- Source range: L240-L240
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.T20` — Prime Polarity Scaling Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T20] Structural: label classification of prime 5 (5 ≡ 1 mod 4 → B). -/
```

## Source Excerpt

```lean
theorem label_5_is_B : label_direct 5 = .B := by native_decide
```
