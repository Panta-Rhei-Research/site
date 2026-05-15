---
{
  "projection_kind": "taulib_declaration",
  "title": "AdeleElement",
  "permalink": "/corpus/taulib/docs/book-iii-spectral-adeles/adele-element/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Spectral.Adeles`.",
  "declaration_id": "TauLib.BookIII.Spectral.Adeles::AdeleElement",
  "declaration_slug": "adele-element",
  "kind": "structure",
  "name": "AdeleElement",
  "module_name": "TauLib.BookIII.Spectral.Adeles",
  "module_url": "/corpus/taulib/docs/book-iii-spectral-adeles/",
  "source_line_start": 38,
  "source_line_end": 41,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L38-L41",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.Adeles",
        "url": "/corpus/taulib/docs/book-iii-spectral-adeles/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L38-L41",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIII.Spectral.Adeles](/corpus/taulib/docs/book-iii-spectral-adeles/)
- Source path: [`TauLib/BookIII/Spectral/Adeles.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L38-L41)
- Source range: L38-L41
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `III.D22` — τ-Adele Ring

## Immediate Comment / Docstring

```lean
/-- [III.D22] An adele element at finite depth: a tuple of local field
    elements, one per prime, with almost all integral (= unit mod p). -/
```

## Source Excerpt

```lean
structure AdeleElement where
  depth : TauIdx               -- number of primes
  components : List TauIdx     -- value mod p_i for each prime
  deriving Repr, DecidableEq, BEq
```
