---
{
  "projection_kind": "taulib_declaration",
  "title": "tauObj_countable",
  "permalink": "/verify/taulib/docs/book-i-orbit-countability/tau-obj-countable/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Countability`.",
  "declaration_id": "TauLib.BookI.Orbit.Countability::tauObj_countable",
  "declaration_slug": "tau-obj-countable",
  "kind": "theorem",
  "name": "tauObj_countable",
  "module_name": "TauLib.BookI.Orbit.Countability",
  "module_url": "/verify/taulib/docs/book-i-orbit-countability/",
  "source_line_start": 73,
  "source_line_end": 76,
  "registry_ids": [
    "I.P04"
  ],
  "related_registry_items": [
    {
      "id": "I.P04",
      "title": "Orbit Countability",
      "url": "/registry/object/I.P04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Countability.lean#L73-L76",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Countability",
        "url": "/verify/taulib/docs/book-i-orbit-countability/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Countability.lean#L73-L76",
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

- Module: [TauLib.BookI.Orbit.Countability](/verify/taulib/docs/book-i-orbit-countability/)
- Source path: [`TauLib/BookI/Orbit/Countability.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Countability.lean#L73-L76)
- Source range: L73-L76
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P04` — Orbit Countability

## Immediate Comment / Docstring

```lean
/-- [I.P04] Obj(τ) is countable: there exists an injection TauObj → Nat. -/
```

## Source Excerpt

```lean
theorem tauObj_countable : ∃ f : TauObj → Nat, Function.Injective f :=
  ⟨tauObj_encode, fun _ _ h => tauObj_encode_injective _ _ h⟩

end Tau.Orbit
```
