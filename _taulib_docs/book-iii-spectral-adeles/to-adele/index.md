---
{
  "projection_kind": "taulib_declaration",
  "title": "to_adele",
  "permalink": "/verify/taulib/docs/book-iii-spectral-adeles/to-adele/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.Adeles`.",
  "declaration_id": "TauLib.BookIII.Spectral.Adeles::to_adele",
  "declaration_slug": "to-adele",
  "kind": "def",
  "name": "to_adele",
  "module_name": "TauLib.BookIII.Spectral.Adeles",
  "module_url": "/verify/taulib/docs/book-iii-spectral-adeles/",
  "source_line_start": 45,
  "source_line_end": 46,
  "registry_ids": [
    "III.D22"
  ],
  "related_registry_items": [
    {
      "id": "III.D22",
      "title": "τ-Adele Ring",
      "url": "/registry/object/III.D22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L45-L46",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.Adeles",
        "url": "/verify/taulib/docs/book-iii-spectral-adeles/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L45-L46",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookIII.Spectral.Adeles](/verify/taulib/docs/book-iii-spectral-adeles/)
- Source path: [`TauLib/BookIII/Spectral/Adeles.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L45-L46)
- Source range: L45-L46
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D22` — τ-Adele Ring

## Immediate Comment / Docstring

```lean
/-- [III.D22] Build an adele element from a global τ-value x at depth k.
    The i-th component is x mod p_{i+1} (using CRT decomposition). -/
```

## Source Excerpt

```lean
def to_adele (x k : TauIdx) : AdeleElement :=
  ⟨k, crt_decompose x k⟩
```
